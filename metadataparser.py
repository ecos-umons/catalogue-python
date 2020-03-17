from os import listdir, environ
import markdown
import requests
import json
from requests.exceptions import HTTPError

file_folder = "content/markdowns/"
md = markdown.Markdown(extensions = ['meta'])

SECRET_KEY = environ.get('SECRET_KEY')


headers = {"Authorization": "token " + SECRET_KEY}

params = {
 "Host" : "pypi.org",
 "Accept" : "application/json"
}


def update_version(pip) :
    url = "http://pypi.org/pypi/" + pip + "/json"
    request = requests.get(url, params)
    try:
        repo = request.json()['releases']
        # If the response was successful, no Exception will be raised
        request.raise_for_status()
        last = list(repo.keys())[-1] #releases should be ordered chronologically
        date = repo[last][0]["upload_time_iso_8601"][:10] # cutting to right format
        return last, date
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}, {request.status_code}')  # Python 3.6
    except Exception as err:
        print(f'Other error occurred: {err}, {request.status_code}')  # Python 3.6


def make_query(query) :
    request = requests.post('https://api.github.com/graphql', json={'query': query}, headers=headers)
    try:
        repo = request.json()["data"]["repository"]
        # If the response was successful, no Exception will be raised
        request.raise_for_status()
        return repo["stargazers"]["totalCount"], repo["forkCount"], repo["issues"]["totalCount"], repo["pullRequests"]["totalCount"]
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}, {request.status_code}')  # Python 3.6
    except Exception as err:
        print(f'Other error occurred: {err}, {request.status_code}')  # Python 3.6

def rewrite_metadata(content, dic):
    new_headers = ""

    body = content.split("\n\n")
    headers = body[0]
    for line in headers.split("\n") :
        has_match = False
        for key in list(dic.keys()) :
            if line.startswith(key) :
                new_headers = new_headers + key + ": " + str(dic[key]) + "\n"
                del dic[key]
                has_match = True
        if not has_match :
            new_headers = new_headers + line + "\n"

    # In case we forgot to add a line manually
    for left in list(dic.keys()) :
        new_headers = new_headers + left + ": " + str(dic[left]) + "\n"

    body[0] = new_headers
    new_txt = "\n\n".join(body)

    return new_txt

def update_fiche(content, temp):
    md.convert(content)
    url = md.Meta['source_url'][0]
    pip = md.Meta['pip'][0]

    latest, version = update_version(pip)

    if "github" in url :
        #Injecting repository identity
        owner, repo = url.replace("https://github.com/", "").split("/")
        query = temp.replace("$owner", "\""+ owner + "\"").replace("$repo", "\""+repo+"\"")

        metadata = make_query(query)

        dic = {
            'Stars' : metadata[0],
            'Forks' : metadata[1],
            'Issues' : metadata[2],
            'Pullrequests' : metadata[3],
            'Latest' :latest,
            'Version' : version,
        }

        return rewrite_metadata(content, dic)
    else :
        print(str(md.Meta["title"]) + " is not using Github.")
        dic = {
            'Latest' : latest,
            'Version' : version,
        }
        return rewrite_metadata(content, dic)



if __name__ == "__main__" :
    with open("ghrequest.json", 'r') as template_file :
        temp = template_file.read()
        for file in listdir(file_folder) :
            with open(file_folder + file, 'r+') as content_file:
                content = content_file.read()
                try :
                    new_text = update_fiche(content, temp)
                    content_file.seek(0)
                    content_file.write(new_text)
                except Exception as e :
                    print(e)

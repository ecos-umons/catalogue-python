from os import listdir, environ
import markdown
import requests
import json
from requests.exceptions import HTTPError

#Only applying the script on content/markdown. Eventually, all content will just be in content/
file_folder = "content/markdowns/"
md = markdown.Markdown(extensions = ['meta'])

#Using the secret_key which allows to pull data from the github API
SECRET_KEY = environ.get('SECRET_KEY')
headers = {"Authorization": "token " + SECRET_KEY}

#Parameters of the pipy request
params = {
 "Host" : "pypi.org",
 "Accept" : "application/json"
}

def update_version(pip) :
    """Based on the pip identifier, returns relevant data about latest release : latest version and date"""

    #Requesting the PyPI api
    url = "http://pypi.org/pypi/" + pip + "/json"
    request = requests.get(url, params)

    #Reading the json and extracting the relevant data
    try:
        repo = request.json()['releases']# If the response was successful, no Exception will be raised
        request.raise_for_status()
        last = list(repo.keys())[-1] #releases should be ordered chronologically (PyPI convention)
        date = repo[last][0]["upload_time_iso_8601"][:10] #Formatting
        return last, date
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}, {request.status_code}')  # Python 3.6
    except Exception as err:
        print(f'Other error occurred: {err}, {request.status_code}')  # Python 3.6


def make_query(query) :
    """ Retrieves stars, fork count, issues and pull requests from Github, using query as query"""

    request = requests.post('https://api.github.com/graphql', json={'query': query}, headers=headers)

    #Try to open the json and extracting the data
    try:
        repo = request.json()["data"]["repository"]# If the response was successful, no Exception will be raised
        request.raise_for_status()
        return repo["stargazers"]["totalCount"], repo["forkCount"], repo["issues"]["totalCount"], repo["pullRequests"]["totalCount"] #formatting
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}, {request.status_code}')  # Python 3.6
    except Exception as err:
        print(f'Other error occurred: {err}, {request.status_code}')  # Python 3.6

def rewrite_metadata(content, dic):
    """From content, which is the old text with the metadata and dic which has the new data, return new_txt which has data replaced by dic content, with relevant headers added """

    #Splitting into headers and body. Technically, body is a list of paragraphs where first one is the headers
    new_headers = ""
    body = content.split("\n\n")
    headers = body[0]

    #Replacing data in headers
    for line in headers.split("\n") :
        has_match = False

        #Replace data in preexisting line
        for key in list(dic.keys()) :
            if line.startswith(key) :
                new_headers = new_headers + key + ": " + str(dic[key]) + "\n"
                del dic[key]
                has_match = True

        #Copies existing header that is not overwrote by dic
        if not has_match :
            new_headers = new_headers + line + "\n"

    # In case we forgot to add a line manually
    for left in list(dic.keys()) :
        new_headers = new_headers + left + ": " + str(dic[left]) + "\n"

    #Formatting, joining new text
    body[0] = new_headers
    new_txt = "\n\n".join(body)

    return new_txt


def update_fiche(content, temp):
    """
    Based on content (which is markdown text) and temp (which is a template of json request),
    returns new data for fiche, based on API calls
    """

    #Read markdown and metadatas
    md.convert(content)
    url = md.Meta['source_url'][0]
    pip = md.Meta['pip'][0]

    #Call PyPI to know about the latest release
    latest, version = update_version(pip)

    dic = {
        'Latest' : latest,
        'Version' : version,
    }

    # Calls the github api (if it is relevant) for additional info
    if "github" in url :
        #Injecting repository identity
        owner, repo = url.replace("https://github.com/", "").split("/")
        query = temp.replace("$owner", "\""+ owner + "\"").replace("$repo", "\""+repo+"\"")

        metadata = make_query(query)

        #Overwrite dic with more extensive data
        dic = {
            'Stars' : metadata[0],
            'Forks' : metadata[1],
            'Issues' : metadata[2],
            'Pullrequests' : metadata[3],
            'Latest' :latest,
            'Version' : version,
        }

    #Returns a string which is the improved text
    return rewrite_metadata(content, dic)



if __name__ == "__main__" :
    #Using a template json file makes updating to new GitHub API specifications easier
    with open("ghrequest.json", 'r') as template_file :
        temp = template_file.read()
        #Treating every markdown
        for file in listdir(file_folder) :
            with open(file_folder + file, 'r+') as content_file:
                content = content_file.read()
                try :
                    #Get improved data and overwrite file
                    new_text = update_fiche(content, temp)
                    content_file.seek(0)
                    content_file.write(new_text)
                except Exception as e :
                    print(e)

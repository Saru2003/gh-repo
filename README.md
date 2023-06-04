# GitHub Repository Analyzer

## Overview

The GitHub Repository Analyzer is a command-line tool that retrieves information about repositories created by a user in a specific year. It takes two parameters, the GitHub username and the year, and provides a list of repositories along with their creation date, link, repository name, and the primary programming language used.

## Usage

### Cloning the Repository

You can clone the repository to your local machine by running the following command:

```bash
git clone https://github.com/Saru2003/gh-repo.git
```
Alternatively, you can download the ZIP file and extract it.

### Installing Dependencies
Before running the tool, ensure that you have the necessary Python modules installed. You can install them by running the following command:
```bash
pip install -r requirements.txt
```

   
### Running the Tool
To use the GitHub Repository Analyzer, execute the following command:

```bash
./gh-repo.py -u <USERNAME> -y <YEAR>
```
Replace <USERNAME> with the desired GitHub username and <YEAR> with the year for which you want to retrieve repository information.

## Docker Image
Alternatively, you can use the provided Docker image to run the tool. Make sure you have Docker installed on your machine. You can either pull the image or run it directly:

Pull the Docker image:

```bash
docker pull sarvesh20123/gh-repo
```

Run the Docker container:
```bash
docker run sarvesh20123/gh-repo -u <USERNAME> -y <YEAR>
```
Please note that the GitHub Repository Analyzer is cross-platform compatible and can be run on Linux, macOS, and Windows systems.

You can find the official Docker image for the GitHub Repository Analyzer on [Docker Hub](https://hub.docker.com/r/sarvesh20123/gh-repo).

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/Saru2003/gh-repo/blob/main/LICENSE) file for details.



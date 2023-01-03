# pyTweetDelete

Delete all the unimportant tweets that you don't like

## Usage

Clone the repo and install the required dependencies:

```bash
git clone https://github.com/chrischriscris/pyTweetDelete.git
cd pyTweetDelete
python -m venv venv # optional
source venv/bin/activate # optional
python -m pip install -r requirements.txt
```

Create a Twitter app and get the API keys from [here](https://developer.twitter.com/en/apps). Add the keys in a `.env` file in the root directory of the project:

```bash
API_KEY=...
API_SECRET=...
ACCESS_TOKEN=...
ACCESS_TOKEN_SECRET=...
```

Run the script:

```bash
python pyTweetDelete.py
```

This will delete all the tweets of your user. You can also delete the tweets with more than a certain number of likes or retweets. To get more information about the options, run:

```bash
python pyTweetDelete.py --help
```

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE.md) file for details.

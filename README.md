# explore-langchain
Repo exploring LangChain 

### Environment Creation and Activation

```bash
python -m venv venv
source venv/bin/activate        # Mac/Linux
venv\Scripts\Activate           # Windows
```

- Initialize git

```bash
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin git@github.com:niweshbaraj/x.git
git push -u origin main
```

- Create a requirements.txt file and install the dependencies with following command :

```bash
pip install -r requirements.txt
```

- Create .env file in the root directory to store secrets and store them like (THIS FILE IS NOT PUSHED TO GITHUB REPO, SO CREATE ONE ON YOUR LOCAL SYSTEM - PUT YOUR-KEY IN UNDER INVERTED COMMA FOR WINDOWS - "YOUR-KEY"):

```bash
OPENAI_API_KEY=YOUR-KEY
ANTHROPY_API_KEY=YOUR-KEY
GOOGLE_API_KEY=YOUR-KEY
HUGGINGFACEHUB_ACCESS_TOKEN=YOUR-KEY
HF_TOKEN=YOUR-KEY
```



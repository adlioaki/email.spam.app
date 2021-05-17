mkdir -p ~/.streamlit/
echo "\
[general]\n\
email = \"zordonbonzo@gmail.com\"\n\
" > ~/.streamlit/credentials.toml
echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT8080\n\
" > ~/.streamlit/config.toml

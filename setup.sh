mkdir -p ~/.streamlit/

echo "\
[server]\n\
headless = true\n\
port = $PORT\n\
enablesCORS = false\n\
\n\
" > ~/.streamlit/config.toml
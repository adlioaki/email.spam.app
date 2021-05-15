mkdir -p ~/.streamlit/

echo "\
[server]\n\
headless = true\n\
port = $PORT5000\n\
enablesCORS = false\n\
headless=true\n\
\n\
" > ~/.streamlit/config.toml

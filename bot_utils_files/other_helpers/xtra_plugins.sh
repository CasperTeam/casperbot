

PLUGIN_REPO="https://github.com/casperteam/unofficial.git"
xtra_fold="./xtraplugins"
req_file="./xtraplugins/req.txt"

make_xtra_dir () {
  if [[ -d "$xtra_fold" ]] 
  then
    rm -r "$xtra_fold"
    mkdir "$xtra_fold"
  else
    mkdir "$xtra_fold"
  fi
}

git_clone_plugin_repo () {
  git clone "$PLUGIN_REPO" "$xtra_fold"
}

xtra_pip_installer () {
    pip3 install --no-cache-dir -r "$req_file"
}

fetch_xtra_plugins () {
  make_xtra_dir
  git_clone_plugin_repo
  xtra_pip_installer
}

fetch_xtra_plugins

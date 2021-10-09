# CICD-pipeline

## What is it ?

This project is a custom pipeline for anyone to use when your project is in **devlopment phase**.
   
   ## working
      
   It is very simple just clones your repo into the folder in the server spacified 
   runs npm i to install all modules 
   restarts pm2 and nginx webserver
   
## How to use ?

1. clone this repo (git clone)
2. set your project repo link and server path where you want you api code to be in the config.py file in pipeline/scripts
3. set your security key in config.js file in pipeline/ci_API
4. host this on your server using reverse proxy nginx 

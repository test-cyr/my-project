# CI/CD with GitHub Actions on AWS EC2

## Project Overview
This project demonstrates setting up a basic CI/CD pipeline for a static website using GitHub Actions and deploying to an EC2 instance with Nginx.

## Features
- Automatic deployment of HTML files from GitHub to EC2
- Git repository initialized on the server for workflow compatibility
- Nginx web server hosting the website
- Basic CI/CD workflow configuration with GitHub Actions

## Screenshots
![Workflow Screenshot](./screenshots/workflow.png)
![Deployed Website](./screenshots/website.png)

## Steps Completed
1. SSH access to EC2 instance
2. Nginx installation and verification
3. Server folder initialized as Git repository (git init + remote add)
4. GitHub Actions workflow created and linked to EC2
5. Local changes pushed and automatically deployed to server

## Next Steps
- Dockerize the web application
- Extend workflow for multi-branch deployment
- Explore CI/CD testing steps

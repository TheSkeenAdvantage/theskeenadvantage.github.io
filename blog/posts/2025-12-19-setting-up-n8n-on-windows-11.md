---
layout: post
title: "Setting Up N8N on Windows 11: A Step-by-Step Guide"
date: 2025-01-10
categories: [automation, n8n, docker, windows]
tags: [n8n, docker, wsl, windows-11, automation]
author: Matt Skeen
description: "A complete step-by-step guide to installing and running N8N on Windows 11 using WSL and Docker, optimized for local automation and development workflows."
---

## Table of Contents
- Step 1: Enable Virtualization on Windows 11
- Step 2: Install Ubuntu on WSL
- Step 3: Install Docker on Ubuntu
- Step 4: Launch N8N with Docker
- Step 5: Access N8N
- What’s Next

---

In the world of automation and workflow management, **N8N** is quickly becoming a go-to solution for businesses and developers alike. N8N is an open-source automation platform that allows you to connect applications, orchestrate workflows, and automate repetitive tasks without writing complex code.

By leveraging integrations with over 200 services, N8N enables teams to reduce operational friction and focus on higher-value work.

This guide walks through setting up **N8N on Windows 11 using Docker and Windows Subsystem for Linux (WSL)**. By the end, you’ll have a fully functional local N8N instance ready for experimentation and workflow development.

---

## Step 1: Enable Virtualization on Windows 11

Docker relies on virtualization to run containers efficiently. Before installing Docker or N8N, ensure your system is correctly configured.

### Preparing Windows

1. Open the Start Menu and search for **“Turn Windows features on or off.”**
2. Ensure the following features are enabled:
   - ✅ Virtual Machine Platform  
   - ✅ Windows Hypervisor Platform  
   - ✅ Windows Subsystem for Linux (WSL)
3. Restart your computer.

> **Pro Tip:** If Docker fails to start, enter your system BIOS and verify that **CPU Virtualization** (Intel VT-x or AMD-V) is enabled.

---

## Step 2: Install Ubuntu on WSL

Ubuntu will act as the Linux environment where Docker and N8N will run.

### Launching Ubuntu

- Search for **Ubuntu** in the Start Menu and launch it.
- On first launch, create a Linux username and password.

You can also start Ubuntu from PowerShell:

```bash
wsl -d Ubuntu
```

### Installing Ubuntu (If Needed)

If Ubuntu is not installed:

1. Open **PowerShell as Administrator**
2. Run:

```bash
wsl --install -d Ubuntu
```

3. Restart your PC if prompted, then launch Ubuntu.

---

## Step 3: Install Docker on Ubuntu

Docker will be used to run N8N in an isolated, portable container.

### Docker Installation

Update the system:

```bash
sudo apt update
sudo apt upgrade
```

Install required packages:

```bash
sudo apt install apt-transport-https ca-certificates curl software-properties-common
```

Add Docker’s official GPG key:

```bash
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
```

Add the Docker repository:

```bash
echo "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list
```

Update packages again:

```bash
sudo apt update
```

Install Docker Engine:

```bash
sudo apt install docker-ce
```

Start and enable Docker:

```bash
sudo systemctl start docker
sudo systemctl enable docker
```

(Optional) Allow Docker to run without sudo:

```bash
sudo usermod -aG docker $USER
```

Log out and log back in for changes to take effect.

Verify Docker:

```bash
docker --version
sudo docker run hello-world
```

For additional details, see the [Docker installation documentation](https://docs.docker.com/engine/install/).

---

## Step 4: Launch N8N with Docker

### Create a Docker Volume

Persist N8N data across container restarts:

```bash
docker volume create n8n_data
```

### Run N8N

```bash
docker run -it --rm   --name n8n   -p 5678:5678   -v n8n_data:/home/node/.n8n   docker.n8n.io/n8nio/n8n
```

- `-it` enables interactive mode
- `--rm` removes the container when stopped
- `-v` mounts persistent storage

If required, prepend commands with `sudo`.

For more information, reference the [N8N documentation](https://docs.n8n.io).

---

## Step 5: Access N8N

Once the container is running, open a browser and navigate to:

```
http://localhost:5678
```

Create your admin account using:
- Email address
- First and last name
- Password

Optionally opt in to security and update notifications.

---

## What’s Next

Your local N8N instance is now live and ready for use.

You can begin by:
- Building simple automation workflows
- Connecting APIs and SaaS platforms
- Experimenting with triggers and webhooks

> ⚠️ **Production Note:**  
> This guide is intended for **local development and testing only**.  
> Production deployments should include:
> - External databases
> - HTTPS and reverse proxies
> - Authentication hardening
> - Secrets management and backups

---

*This post is part of an ongoing automation and cloud engineering series.*

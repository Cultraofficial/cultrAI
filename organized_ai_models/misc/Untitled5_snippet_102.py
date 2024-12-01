# Add the Google Cloud apt repository
!curl -fsSL https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
!echo "deb https://apt.kubernetes.io/ kubernetes-xenial main" | sudo tee -a /etc/apt/sources.list.d/kubernetes.list

# Update package listings and install kubectl
!apt-get update
!apt-get install -y kubectl

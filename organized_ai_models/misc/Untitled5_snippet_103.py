# Download the latest kubectl binary
!curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"

# Make the kubectl binary executable
!chmod +x kubectl

# Move the binary into your PATH
!sudo mv kubectl /usr/local/bin/

# Verify the installation
!kubectl version --client

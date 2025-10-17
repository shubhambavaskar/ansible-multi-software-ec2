# DevOps Project: Multi-Software Installation and EC2 Monitoring using Ansible

📌 **Project Objective**
Automate the installation, configuration, updates, and monitoring of multiple software packages across 150+ AWS EC2 instances using Ansible.

---

🛠️ **Tools Used**

* Ansible – for automation of software installation and configuration
* AWS EC2 – to host and manage multiple instances
* Git & GitHub – for version control and code repository
* Docker – for containerization of software services
* Jenkins – for CI/CD integration and automation
* Git – source code management
* Terraform – for infrastructure provisioning
* Nginx – web server configuration

---

🔧 **Project Workflow**

**1️⃣ Inventory and EC2 Setup**

* Define EC2 instances in Ansible inventory file
* Group servers based on roles (e.g., web, CI/CD, monitoring)

**2️⃣ Multi-Software Installation**

* Install and configure:

  * Docker – container runtime for applications
  * Jenkins – CI/CD automation server
  * Git – version control
  * Nginx – web server
* Ensure consistent versions and configurations across all servers

**3️⃣ Automated Updates**

* Regular updates of installed software using Ansible playbooks
* Reduced manual intervention and ensured all servers remain up-to-date

**4️⃣ EC2 Monitoring (via Ansible)**

* Collect system metrics from all EC2 instances using Ansible playbooks:

  * Disk usage
  * CPU usage
  * Memory utilization
  * Running processes
* Centralized reporting for better infrastructure visibility

**5️⃣ Integration with GitHub**

* Store Ansible playbooks in GitHub repository
* Enable version control and collaboration

---

📂 **Project File Structure**

```
ansible-multi-software-ec2/
├── ansible.cfg             # Ansible configuration file
├── inventory.ini           # EC2 inventory list and grouping
├── playbooks/
│   ├── install_software.yml  # Installs Docker, Jenkins, Git, Nginx
│   ├── update_software.yml   # Updates all software packages
│   └── monitor_ec2.yml       # Collects system metrics from EC2 instances using Ansible
├── README.md               # Project documentation
```

---

✅ **Outcome**

* Streamlined software management across 150+ EC2 instances
* Centralized monitoring of system metrics using Ansible
* Reduced manual effort and eliminated configuration inconsistencies
* Improved deployment speed and operational efficiency

---

🔗 **GitHub Repository**

[https://github.com/shubhambavaskar/ansible-multi-software-ec2](https://github.com/shubhambavaskar/ansible-multi-software-ec2)

---

## 🙌 Author

**Shubham Bavaskar**
*DevOps | AWS | Cloud Enthusiast*

🔗 [GitHub Profile](https://github.com/shubhambavaskar) | 🔗 [LinkedIn Profile](https://www.linkedin.com/in/shubham-bavaskar-933a75195) | 📧 [Email](mailto:shubhamba97@gmail.com)

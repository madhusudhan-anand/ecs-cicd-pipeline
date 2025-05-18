# 🚀 ECS Fargate CI/CD Pipeline with AWS DevOps

This project demonstrates a full production-grade CI/CD pipeline using AWS services to deploy a containerized Flask app to ECS Fargate. All infrastructure is defined using CloudFormation (Infrastructure as Code).

---

## 📦 Tech Stack

- **Flask** – Python web app  
- **Docker** – Containerization  
- **Amazon ECR** – Container registry  
- **Amazon ECS (Fargate)** – Serverless container hosting  
- **Application Load Balancer** – HTTP routing  
- **AWS CodePipeline** – CI/CD orchestration  
- **AWS CodeBuild** – Image building and deployment  
- **AWS CloudFormation** – Infrastructure as Code (IaC)  
- **GitHub** – Source repository  

---

## 🧠 Architecture Diagram

```
GitHub (main branch)
        │
        ▼
  AWS CodePipeline
        │
        ▼
  AWS CodeBuild (Docker image build)
        │
        ▼
    Amazon ECR (image pushed)
        │
        ▼
  AWS ECS Fargate (new task launched)
        │
        ▼
Application Load Balancer (public URL)
```

---

## ✅ Features

- Full CI/CD from GitHub push to ECS deployment  
- Secure ECR authentication  
- CloudWatch logging  
- Health-checked ALB  
- Infrastructure-as-Code using YAML  

---

## 📝 Deployment Steps

### 1. 🛠 Clone this repo

```bash
git clone https://github.com/yourusername/ecs-cicd-pipeline.git
cd ecs-cicd-pipeline
```

### 2. ☁️ Deploy CloudFormation stacks

#### Deploy VPC stack:

```bash
# Upload cloudformation/vpc.yml via CloudFormation
```

#### Deploy ECS stack:

```bash
# Upload cloudformation/ecs-cluster.yml via CloudFormation
# Provide VPC, Subnets, Security Group from vpc-stack outputs
```

### 3. 🔧 Create and Deploy Pipeline

- Update `pipeline.yml` with your GitHub repo, branch, and ECR URI  
- Deploy using CloudFormation

---

## 📂 Folder Structure

```
ecs-cicd-pipeline/
├── app/                    # Flask app
│   ├── app.py
│   └── Dockerfile
├── buildspec.yml           # Instructions for CodeBuild
├── cloudformation/
│   ├── vpc.yml             # VPC, Subnets, Security Group
│   └── ecs-cluster.yml     # ECS cluster, ALB, Task, Service
├── pipeline.yml            # CodePipeline + CodeBuild
```

---

## 📸 Screenshots

| Screenshot | Description |
|------------|-------------|
| ✅ ALB browser output | App running at LoadBalancer DNS |
| ✅ CodePipeline view | All stages green |
| ✅ ECS Service | Running task in ECS |
| ✅ ECR image | Image tagged with commit hash |
| ✅ CloudWatch Logs | Shows Flask app starting up |

---

## 🚀 Live Demo

> http://ecs-st-loadb-gzeyqj69y1cu-1489915268.us-east-1.elb.amazonaws.com/

> Check Screenshots for result

---

## 🧠 Lessons Learned

- Using `buildspec.yml` for CodeBuild clarity  
- IAM permissions for ECS deployments  
- Managing YAML indentation and escaping in CF templates  
- Debugging container health with ALB and CloudWatch  

---

## 🙌 Author

**Madhusudhan Anand**  
AWS Certified Solutions Architect | DevOps Practitioner  
[LinkedIn](www.linkedin.com/in/
madhusudhananand) • [GitHub](https://github.com/madhusudhan-anand)

---

## 📜 License

MIT – free to use and modify.

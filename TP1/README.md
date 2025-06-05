# OpenFaaS TP1 - Déploiement et Utilisation

## Prérequis

- [Docker](https://www.docker.com/products/docker-desktop)
- [Minikube](https://minikube.sigs.k8s.io/docs/)
- [kubectl](https://kubernetes.io/docs/tasks/tools/)
- [Helm](https://helm.sh/)
- [faas-cli](https://docs.openfaas.com/cli/install/)

---

## 1. Lancer Minikube

```sh
minikube start
```

---

## 2. Installer OpenFaaS avec Helm

```sh
kubectl create namespace openfaas
kubectl create namespace openfaas-fn

helm repo add openfaas https://openfaas.github.io/faas-netes/
helm repo update

helm upgrade openfaas --install openfaas/openfaas \
  --namespace openfaas \
  --set functionNamespace=openfaas-fn \
  --set generateBasicAuth=true
```

---

## 3. Accéder à la Gateway OpenFaaS

```sh
kubectl port-forward -n openfaas svc/gateway 8082:8080
```
> **L’interface graphique sera accessible sur :**  
> [http://127.0.0.1:8082](http://127.0.0.1:8082)

---

## 4. Récupérer le mot de passe admin

```sh
PASSWORD=$(kubectl get secret -n openfaas basic-auth -o jsonpath="{.data.basic-auth-password}" | base64 --decode)
```

---

## 5. Se connecter avec faas-cli

```sh
faas-cli login -g http://127.0.0.1:8082 -u admin -p $PASSWORD
```

---

## 6. Déployer les fonctions

Dans le dossier du projet, exécute :

```sh
faas-cli deploy -f save-feedback.yml
faas-cli deploy -f get-quote.yml
```

---

## 7. Vérifier les fonctions déployées

```sh
faas-cli list -g http://127.0.0.1:8082
```

---

## 8. Tester les fonctions

Par exemple, pour tester la fonction `get-quote` :

```sh
curl http://127.0.0.1:8082/function/get-quote
```

Pour `save-feedback` (POST) :

```sh
curl -X POST http://127.0.0.1:8082/function/save-feedback -d '{"feedback":"super !"}' -H "Content-Type: application/json"
```

---

## 9. Arrêter l’environnement

```sh
minikube stop
```

---

## Structure du projet

- `save-feedback.yml` et `get-quote.yml` : fichiers de déploiement des fonctions
- `save-feedback/`, `get-quote/` : code source des fonctions
- `build/` : artefacts de build (générés)
- `template/` : templates OpenFaaS pour différents langages

---

**Auteur :** Yohan  MARTIN
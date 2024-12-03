
# gen3-helm-uf-cancer-data-center

This is uf cancer-data-center application development code using gen3. To start helm deployment:
```
minikube start --kubernetes-version v1.27.11 --memory 24g --cpus 4
sudo sysctl -w vm.max_map_count=262144
helm upgrade --install gen3 ./helm/gen3 -f ./ufcdc_config/major_config/gen3_config_v7_less_downlaod_options.yaml
```
Then create program node and project node, and instructions is same as [this](https://github.com/Su-informatics-lab/ardac/blob/master/helm/docs/rancher-desktop.md), then upload tsv files in [demo-data](./demo-data) folder following same guidelines as [this](https://github.com/Su-informatics-lab/ardac/blob/master/helm/docs/rancher-desktop.md).
```
minikube service revproxy-service --url
sudo vi /etc/caddy/Caddyfile
sudo systemctl restart caddy
```

During data uploading process, you may encounter issues with not having enough sheepdog services to handle large volumns of uploading, you may scale up number of sheepdog services:
```
kubectl scale --replicas=3 deployment/sheepdog-deployment
```
But remember to scale back when finished:
```
kubectl scale --replicas=1 deployment/sheepdog-deployment
kubectl delete pod --field-selector=status.phase==Succeeded
kubectl scale --replicas=1 deployment/requestor-deployment
```

Now the ETL job needs to be started:
```
kubectl create job --from=cronjob/etl-cronjob etl
```

Verify the job for etl completes in k9s. You can also curl the indices on the elasticsearch endpoint. Like so (make sure
to replace the pod name with what is in k9s)

```
kubectl exec -it portal-deployment-77d9bc4df4-zdssw -- bash
curl -X GET http://gen3-elasticsearch-master:9200/_cat/indices?v
```

If you want to rerun etl process, please delete previous elastic indices before executing again:
```
kubectl exec -it portal-deployment-77d9bc4df4-zdssw -- bash
curl -X DELETE 'http://gen3-elasticsearch-master:9200/_all'
```

Now guppy can be started;
now start guppy:

```
in ./helm/guppy:  helm dependency update;helm dependency build
in ./gen3-helm-ufcdc: helm upgrade --install guppy ./helm/guppy -f ./ufcdc_config/guppy_config/rancher-desktop-values-guppy.yaml
```



The original tutorials for deploying gen3-helm: [https://github.com/uc-cdis/gen3-helm/blob/master/README.md].

kubectl delete pod --field-selector=status.phase==Succeeded

kubectl scale --replicas=3 deployment/sheepdog-deployment

other codes I used myself:

```
  tierAccessLevel: "regular"

  kubectl get pods --all-namespaces
  kubectl get nodes --show-labels
  kubectl label nodes minikube role=jupyter
  kubectl describe pod hatchery-minghaozhou01-40gmail-2ecom -n jupyter-pods-gen3

  cd ./gen3-helm/helm/gen3
  helm dependency build .

  resart services related to security and accessibility:

  kubectl rollout restart deployment fence-deployment
  kubectl rollout restart deployment arborist-deployment
  kubectl rollout restart deployment guppy-deployment

  docker build -t minghaozhou01/cancer_commons_portal:v9 .
  docker push minghaozhou01/cancer_commons_portal:v9
  docker rmi -f $(docker images -q)

  docker rmi --all --force

  helm upgrade --install gen3 ./helm/gen3 -f /home/exouser/gen3-helm-ufcdc/ufcdc_config/major_config/gen3_config_v7_less_downlaod_options.yaml

  helm upgrade --install gen3 gen3/gen3 -f /home/exouser/gen3-helm-ufcdc/ufcdc_config/major_config/gen3_config_v7_less_downlaod_options.yaml

  to run local deployment
  npm ci
  HOSTNAME=ufcdc-portal.org APP=config NODE_ENV=dev bash ./runWebpack.sh
  sudo sysctl fs.inotify.max_user_watches=524288
  NODE_OPTIONS=--openssl-legacy-provider HOSTNAME=ufcdc-portal.org APP=config NODE_ENV=dev bash ./runWebpack.sh

  poetry run alembic revision --autogenerate -m "Your migration message"

  docker build -t minghaozhou01/cancer_commons_requestor:v3 .
  docker push minghaozhou01/cancer_commons_requestor:v3
  docker rmi -f $(docker images -q)
  
  printenv
  POSTGRES_PASSWORD=???
  \l
  \c requestor_gen3
```
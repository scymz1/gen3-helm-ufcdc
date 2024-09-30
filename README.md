
# gen3-helm-uf-cancer-data-center

This is uf cancer-data-center application development code using gen3. To start helm deployment:
```
minikube start --kubernetes-version v1.27.11 --memory 24g --cpus 4
sudo sysctl -w vm.max_map_count=262144
helm upgrade --install gen3 ./helm/gen3 -f ./ufcdc_config/gen3_config_new.yaml
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
```

Now the ETL job needs to be started:
```
kubectl create job --from=cronjob/etl-cronjob etl
```

Verify the job for etl completes in k9s. You can also curl the indices on the elasticsearch endpoint. Like so (make sure
to replace the pod name with what is in k9s)

```
kubectl exec -it portal-deployment-5f84b7b6b8-g5chw -- bash
curl -X GET http://gen3-elasticsearch-master:9200/_cat/indices?v
```

If you want to rerun etl process, please delete previous elastic indices before executing again:
```
kubectl exec -it portal-deployment-58d5b54b89-sfd5w -- bash
curl -X DELETE 'http://gen3-elasticsearch-master:9200/_all'
```

Now guppy can be started;
now start guppy:

```
in ./helm/guppy:  helm dependency update;helm dependency build
in ./gen3-helm-ufcdc: helm upgrade --install guppy ./helm/guppy -f ./ufcdc_config/rancher-desktop-values-guppy.yaml
```



The original tutorials for deploying gen3-helm: [https://github.com/uc-cdis/gen3-helm/blob/master/README.md].

kubectl delete pod --field-selector=status.phase==Succeeded

kubectl scale --replicas=3 deployment/sheepdog-deployment



  tierAccessLevel: "regular"

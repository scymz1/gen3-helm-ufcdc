
# gen3-helm-uf-cancer-data-center

This is uf cancer-data-center application development code using gen3. To start helm deployment:
```
helm upgrade --install gen3 ./helm/gen3 -f ./ufcdec_config/gen3_config_new.yaml
```
Then create program node and project node, and instructions is same as [this](https://github.com/Su-informatics-lab/ardac/blob/master/helm/docs/rancher-desktop.md), then upload tsv files in [demo-data](./demo-data) folder following same guidelines as [this](https://github.com/Su-informatics-lab/ardac/blob/master/helm/docs/rancher-desktop.md).

Now the ETL job needs to be started:
```
kubectl create job --from=cronjob/etl-cronjob etl
```

Verify the job for etl completes in k9s. You can also curl the indices on the elasticsearch endpoint. Like so (make sure
to replace the pod name with what is in k9s)

```
kubectl exec -it portal-deployment-74b89bd75f-r8lcc -- bash
curl -X GET http://gen3-elasticsearch-master:9200/_cat/indices?v
```

Now guppy can be started;
now start guppy:

```
in ./helm/guppy:  helm dependency update;helm dependency build
in ./gen3-helm-ufcdc: helm upgrade --install guppy ./helm/guppy -f ./ufcdc_config/rancher-desktop-values-guppy.yaml
```



The original tutorials for deploying gen3-helm: [https://github.com/uc-cdis/gen3-helm/blob/master/README.md].


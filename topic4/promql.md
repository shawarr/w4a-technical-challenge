default grafana dashboards weren't working, so i set up my own dashboard to reflect these values, i dont know how to write promql queries so i got the help of an LLM to write these just to showcase that the grafana dashboard works and is getting data from prometheus.

count(kube_pod_info{namespace="strawberry", pod=~"web-app.\*"})
count number of pods in the namespace

kube_pod_status_phase{namespace="strawberry", phase="Running"}
shows pods that are currently in the running phase

sum by (phase) (kube_pod_status_phase{namespace="strawberry"})
Aggregate pods by their phase to see the count of pods in each status.

kube_deployment_status_replicas_available{namespace="strawberry"}
Show how many replicas are available for deployment.

sum(container_memory_working_set_bytes{namespace="strawberry"})
um the memory currently being used by containers in the namespace.

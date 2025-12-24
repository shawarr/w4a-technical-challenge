#!/bin/bash
NAMESPACE="strawberry"
DEPLOYMENT_LABEL="app.kubernetes.io/name=strawberry"
SEARCH_TERM="Invalid credentials"

PODS=$(kubectl get pods -l $DEPLOYMENT_LABEL -n $NAMESPACE -o jsonpath="{.items[*].metadata.name}")

if [ -z "$PODS" ]; then
    echo "No pods are available in namespace $NAMESPACE with label $DEPLOYMENT_LABEL" 
    exit 1
fi

for POD in $PODS; do
    echo "Checking for invalid auth in $POD"
    kubectl logs -n $NAMESPACE $POD  | grep -i "$SEARCH_TERM" || echo "No invalid login attempts"
    

done
echo "Search complete"

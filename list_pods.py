from kubernetes import client, config                                                                                                                                                                                            
                                                                                                                                                                                                                                 
                                                                                                                                                                                                                                 
def main():
  K8S_NAMESPACE = os.getenv("K8S_NAMESPACE")
                                                                                                                                                                                                                                 
  config.load_incluster_config()                                                                                                                                                                                               
  v1 = client.CoreV1Api()                                                                                                                                                                                                      
                                                                                                                                                                                                                                
  print("Listing pods with their IPs:")                                                                                                                                                                                        
  ret = v1.list_namespaced_pod(K8S_NAMESPACE, watch=False)
  for i in ret.items:
      print("%s\t%s\t%s" %
            (i.status.pod_ip, i.metadata.namespace, i.metadata.name))                                                                                                                                                     
                                                                                                                                                                                                                                 
                                                                                                                                                                                                                                 
if __name__ == '__main__':                                                                                                                                                                                                       
  main()                                                                                                                                                                                                                         
             
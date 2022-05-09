package com.example.gateway;

import org.springframework.cloud.client.ServiceInstance;
import org.springframework.cloud.loadbalancer.annotation.LoadBalancerClients;
import org.springframework.cloud.loadbalancer.core.RandomLoadBalancer;
import org.springframework.cloud.loadbalancer.core.ReactorLoadBalancer;
import org.springframework.cloud.loadbalancer.core.ServiceInstanceListSupplier;
import org.springframework.cloud.loadbalancer.support.LoadBalancerClientFactory;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.core.env.Environment;

@Configuration
@LoadBalancerClients(defaultConfiguration = LoadBConfiguration.class)
public class GatewayConfig {}

class LoadBConfiguration {

   @Bean
   public ReactorLoadBalancer<ServiceInstance> config(
           Environment env, LoadBalancerClientFactory lc) {
       String name = env.getProperty(LoadBalancerClientFactory.PROPERTY_NAME);
       return new RandomLoadBalancer(lc.getLazyProvider(name,
               ServiceInstanceListSupplier.class), name);
   }

}
package com.example.ms_patient.proxies;

import com.example.ms_patient.models.Ordonnance;
import org.springframework.cloud.loadbalancer.annotation.LoadBalancerClient;
import org.springframework.cloud.openfeign.FeignClient;
import org.springframework.data.repository.query.Param;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;

import java.util.List;

@FeignClient(name="ms-ordonnace")
@LoadBalancerClient(name = "ms-ordonnance")
public interface OrdonnanceProxy {
    @GetMapping("/ordonnances/search/getOrdonnancesByPatientId")
    public List<Ordonnance> getOrdonnanceByPatientId(@Param("idp") Long idp);
}

@FeignClient(name="ms-formation")
@LoadBalancerClient(name="ms-formation")

public interface FormationProxy {

@GetMapping("/formations/{id}")
@Bulkhead(name="fall1", fallbackMethod = "fallbackFormation")

FormationDTO getFormation(@PathVariable("id") Long idf);

default FormationDTO fallbackFormation(Long idf, Throwable throwable) {
return new FormationDTO(idf,"php",0) ;
}
}
package com.example.ms_ordonnance.repositories;
import com.example.ms_ordonnance.entities.Ordonnance;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.repository.query.Param;
import org.springframework.data.rest.core.annotation.RepositoryRestResource;

import java.util.List;

@RepositoryRestResource
public interface OrdonnanceRepository extends JpaRepository<Ordonnance,Long> {
    public List<Ordonnance> getOrdonnancesByPatientId(@Param("idp") Long idp);
}

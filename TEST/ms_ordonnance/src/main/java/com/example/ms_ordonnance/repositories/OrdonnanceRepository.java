package com.example.ms_ordonnance.repositories;
import com.example.ms_ordonnance.entities.Ordonnance;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.rest.core.annotation.RepositoryRestResource;

@RepositoryRestResource
public interface OrdonnanceRepository extends JpaRepository<Ordonnance,Long> {
}

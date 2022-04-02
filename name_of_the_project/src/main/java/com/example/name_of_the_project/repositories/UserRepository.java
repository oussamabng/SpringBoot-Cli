package com.example.name_of_the_project.repositories;
import com.example.name_of_the_project.entities.User;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.rest.core.annotation.RepositoryRestResource;

@RepositoryRestResource
public interface UserRepository extends JpaRepository<User,Long> {
}

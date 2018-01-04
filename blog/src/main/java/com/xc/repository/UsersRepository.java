package com.xc.repository;

import com.xc.properties.Users;
import org.springframework.data.jpa.repository.JpaRepository;

/**
 * Created by xiongchi on 2017/11/1.
 */
public interface UsersRepository extends JpaRepository<Users, Integer> {

    Users findByUserName(String userName);

}

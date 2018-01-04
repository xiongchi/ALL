package com.xc.service;

import com.xc.properties.Users;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import com.xc.repository.*;

/**
 * Created by xiongchi on 2017/11/1.
 */
@Service
public class UsersService {

    @Autowired
    private UsersRepository usersRepository;

    public Users getUsersByName(String userName){
        Users user = usersRepository.findByUserName(userName);
        return user;
    }


}

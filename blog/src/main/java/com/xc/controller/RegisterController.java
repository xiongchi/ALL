package com.xc.controller;

import com.xc.consts.Consts;
import com.xc.domain.Result;
import com.xc.properties.Users;
import com.xc.repository.UsersRepository;
import com.xc.utils.MD5util;
import com.xc.utils.ResultUtil;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;

import javax.servlet.http.HttpSession;
import java.util.Map;

/**
 * Created by xiongchi on 2017/11/3.
 * 用于用户注册
 */
@Controller
public class RegisterController {

    @Autowired
    private UsersRepository usersRepository;

    /**
     * 进入注册界面
     * @return
     */
    @RequestMapping(value = "/enterRegister")
    public String enterRegister(){
        return "/register";
    }

    /**
     * 注册
     * @param map
     * @return
     */
    @ResponseBody
    @RequestMapping(value = "/register")
    public Result registerUser(@RequestParam Map<String,Object> map, HttpSession session){

        String userIdty = (String) map.get("userIdty");
        String userName = (String) map.get("userName");
        String userPwd = (String) map.get("userPwd");
        String checkPwd = (String)map.get("checkPwd");
        Users manager = new Users();
        if(!userPwd.trim().equals(checkPwd)){
            return ResultUtil.error(0,"两次密码不一致");
        }
        if(Consts.MANAGER.equals(userIdty)){
            manager.setRoleId(0);
        }else if(Consts.USERS.equals(userIdty)){
            manager.setRoleId(1);
        }
        String encodePwd = MD5util.encode(userPwd);
        manager.setUserName(userName);
        manager.setUserPwd(encodePwd);
        Users u = usersRepository.save(manager);
        session.setAttribute("userId", u.getUserId());
        session.setAttribute("userIdty",userIdty);
        session.setAttribute("userName", userName);
        return ResultUtil.success(1,"注册成功");
    }

}

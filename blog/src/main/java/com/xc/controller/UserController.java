package com.xc.controller;

import com.xc.domain.Result;
import com.xc.properties.Users;
import com.xc.service.UsersService;
import com.xc.utils.MD5util;
import com.xc.utils.ResultUtil;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.*;
import org.apache.commons.lang.*;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpSession;
import javax.validation.Valid;
import java.util.Map;

/**
 * Created by xiongchi on 2017/10/31.
 * 用于用户登录
 */
@Controller
@RequestMapping("/blog")
public class UserController {


    @Autowired
    private UsersService usersService;
    /**
     * 进入登录界面
     * @return
     */
    @RequestMapping(value = "/login")
    public String enterLogin(){
        return "/login";
    }

    /**
     * 用户登录
     * @param users
     * @param bindingResult
     * @return
     */
    @ResponseBody
    @RequestMapping(value = "/userLogin",method = RequestMethod.POST)
    public Result userLogin(@Valid Users users, BindingResult bindingResult, HttpServletRequest request){

        HttpSession session = request.getSession();
        if (bindingResult.hasErrors()) {
            return ResultUtil.error(0, bindingResult.getFieldError().getDefaultMessage());
        }
        String userName = users.getUserName();
        String userPwd = users.getUserPwd();
        Integer roleId = users.getRoleId();
        Users user = usersService.getUsersByName(userName);
        //密码加密
        String encodePwd = MD5util.encode(userPwd);
        if(user.getUserPwd().equals(encodePwd) && roleId == user.getRoleId()){
            session.setAttribute("userName",user.getUserName());
            session.setAttribute("userIdty",user.getRoleId());
            session.setAttribute("userId",user.getUserId());
            return ResultUtil.success(1, "登录成功");
        }else{
            return ResultUtil.error(0, "用户名或密码错误");
        }

    }

    /**
     * 判断用户名是否存在
     * @param userName
     * @return
     */
    @ResponseBody
    @GetMapping(value = "/userCheck")
    public Result userCkeck(@RequestParam String userName){
        if(StringUtils.isBlank(userName)){
            return ResultUtil.error(0, "用户为空");
        }else{
            Users user = usersService.getUsersByName(userName);
            if(user == null){
                return ResultUtil.error(0, "用户名不存在");
            }else {
                return ResultUtil.success(1, "用户名正确");
            }
        }
    }

}

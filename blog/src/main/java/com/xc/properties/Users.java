package com.xc.properties;

import org.hibernate.validator.constraints.NotEmpty;

import javax.persistence.*;

/**
 * Created by xiongchi on 2017/10/31.
 */
@Entity
@Table(name = "users")
public class Users {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "user_id")
    private Integer userId;
    //用户姓名
    @NotEmpty(message = "用户名为空")
    @Column(name = "user_name")
    private String userName;
    //用户密码
    @NotEmpty(message = "密码为空")
    @Column(name = "user_pwd")
    private String userPwd;

    //身份id
    @Column(name = "role_id")
    private Integer roleId;


    public Integer getRoleId() {
        return roleId;
    }

    public void setRoleId(Integer roleId) {
        this.roleId = roleId;
    }

    public Integer getUserId() {
        return userId;
    }

    public void setUserId(Integer userId) {
        this.userId = userId;
    }

    public String getUserName() {
        return userName;
    }

    public void setUserName(String userName) {
        this.userName = userName;
    }

    public String getUserPwd() {
        return userPwd;
    }

    public void setUserPwd(String userPwd) {
        this.userPwd = userPwd;
    }


    @Override
    public String toString() {
        return "Users{" +
                "userId=" + userId +
                ", userName='" + userName + '\'' +
                ", userPwd='" + userPwd + '\'' +
                '}';
    }
}

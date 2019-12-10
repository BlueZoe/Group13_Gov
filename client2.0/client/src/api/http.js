import axios from "axios"
import { Message, MessageBox } from 'element-ui';
import router from "@/router/index"
axios.defaults.baseURL = "http://127.0.0.1:5000/api";
let status = false;

axios.interceptors.request.use(config => {
    let isLogin = localStorage.getItem("login");
    let token = localStorage.getItem("token");
    if(token){
        config.headers.Authorization = token;
    }
    return config;
}, error => {
    return Promise.reject(error);
})


axios.interceptors.response.use(response => {
    if (response.status == 200) {
        response = response.data;
        return response;
    } else {
        Message.error("请求失败,请重新尝试");
    }
}, error => {
    if (error.response.status == 401 && !status) {
        status = true;
        MessageBox.confirm('确认退出？', '提示', {
            confirmButtonText: '确定',
            cancelButtonText: '取消',
            type: 'warning'
        }).then(() => {
            status = false;
            localStorage.removeItem("login");
            router.push({ name: "login" });
        }).catch(() => {
            status = false;
            return Promise.reject(error);
        });
    } else {
        return Promise.reject(error);
    }

})


export default axios;
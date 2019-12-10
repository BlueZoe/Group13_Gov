import axios from "./http"



export default {
    login(params){
        return axios.post("/login",params);
    },
    getNowInfo(){
        return axios.get("/nowData");
    },
    getTopData(){
        return axios.get("/getTopData")
    },
    getManyData(params){
        return axios.get("/getManyData",{params})
    },
    getMonyDataInfo(params){
        return axios.post('/getMonyDataInfo',params)
    },
    getBeforeData(params){
        return axios.get("/beforeData",{params});
    },
    topData(params){
        return axios.post('/topData',params);
    },
    removeData(params){
        return axios.post('/removeData',params);
    },
    getEmergency(){
        return axios.get('/getEmergency');
    }
}
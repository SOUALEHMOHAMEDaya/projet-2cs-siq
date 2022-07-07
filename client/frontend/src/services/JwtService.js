import VueJwtDecode from "vue-jwt-decode";

export const decodeToken = (token) => {
    return VueJwtDecode.decode(token);
}





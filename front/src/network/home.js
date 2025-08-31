import { request } from "./requestConfig"



export function getMainMenu() {
    return request({
        url: "/main_menu/index",
    })
}


export function getSecondMenu(mainMenuId) {
    return request({
        url: "/sub_menu?main_menu_id=" + mainMenuId,
    })
}


export function getFindGoods() {
    return request({
        url: "/goods/find",
    })
}

export function getCategoryGoods(categoryId, page) {
    return request({
        url: "/goods/category/" + categoryId + "/" + page,
    })
}
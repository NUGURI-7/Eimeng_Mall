<template>

    <div>
        <Shortcut></Shortcut>
        <div>我是 主页</div>











    </div>

</template>


<script setup>
import { getMainMenu } from '@/network/home';
import Shortcut from '@/components/common/Shortcut.vue';

const mainList = getMainMenu().then(res => {
    console.log(res);
    return res
})


</script>
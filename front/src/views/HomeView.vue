<template>
    <div>
        我是主页
    </div>
    <div>
        {{ mainList }}
    </div>

</template>


<script setup>
import { getMainMenu } from '@/network/home';
import  {ref } from 'vue'
const mainMenu = ref()

const mainList = getMainMenu().then(res => {
    console.log(res);
    return res
})


</script>
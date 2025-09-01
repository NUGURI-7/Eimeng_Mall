<template>
    <div class="warpper">
        <div class="header">
            <a href="#">你好,请登录</a>
            <a href="#" class="register">免费注册</a> &nbsp;&nbsp;|
            <a href="#">我的订单</a>
        </div>
    </div>
</template>


<script setup>



</script>

<style lang="less" scoped>
.warpper {
    background-color: #e0e5e9;
    height: 30px;

    .header {
        width: var(--content-width);
        margin: 0 auto;
        text-align: right;
        line-height: 30px;

        a {
            color: var(--font-gray);

            &:hover {
                color: chocolate;
            }

            ;
            margin-left: 10px;
        }

        .register {
            color: crimson;
        }
    }
}
</style>
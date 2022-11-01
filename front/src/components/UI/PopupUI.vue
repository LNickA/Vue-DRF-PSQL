<template>
    <div class="popup" v-if="show" @click="$emit('update:show', false)">
        <div @click.stop class="popup__container">
            <slot></slot>
        </div>
    </div>
</template>
<script>
export default {
    name: 'PopupUI',
    props:{
        show: {
            type: Boolean,
            default:false
        }
    },
    methods:{
    }
}
</script>
<style scoped>
.popup{
    top:0;
    bottom: 0;
    right: 0;
    left: 0;
    background: rgba(0,0,0,0.5);
    position: fixed;
    display: flex;
}
.popup__container{
    margin: auto;
    background: white;
    border-radius: 15px;
    padding: 20px;
    width: 33%;
}
</style>
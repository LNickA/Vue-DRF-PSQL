<template>
    <button class="btn" >
        <slot></slot>
    </button>
</template>
    
<script>
        export default {
            name:'ButtonUI',
            data(){
                return{
                    isClicked:false
                }
                
            },
        }
</script>
    
<style scoped>
.btn{
        align-self: flex-end;
        padding: 16px 32px;
        border-radius: 50px;
        border: none;
        color: #b3b3b3;
        font-weight: bold;
      }
</style>
<template>
    <input :value='modelValue' @input="$emit('update:modelValue', $event.target.value)" class="input" type="text">
</template>

<script>
    export default {
        name:'InputUI',
        props:{
           modelValue: [String,Number]
        },
        
        methods:{
        }
    }
</script>

<style scoped>
.input{
    width: 100%;
    border: 1px solid #ECECEC;
    border-radius: 50px;
    padding: 16px 32px;
    margin-bottom: 15px;
  }
</style>
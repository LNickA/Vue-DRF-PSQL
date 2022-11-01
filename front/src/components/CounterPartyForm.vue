<template>
    <div>
        <h3>Добавление контрагента</h3>
        <form @submit.prevent>
            <InputUI
              v-model.trim="counterparty.name"
              type="text"
              placeholder="Имя контрагента"/>
            <ButtonUI @click="createCounterParty" class="btn">Создать</ButtonUI>
        </form>
    </div>
</template>
<script>
import ButtonUI from './UI/ButtonUI.vue';
import InputUI from './UI/InputUI.vue';

export default {
    components:{
        InputUI, ButtonUI
    },
    data(){
        return{
            counterparty: {
                name:"",
                cost:"Отсутствует",
            }
        };
    },
    methods:{
        createCounterParty(){ 
            this.counterparty.id=Date.now();
            this.$emit("create", this.counterparty);
            this.counterparty = {         
                name:'',
            };
        }
    }
}
</script>
<style scoped>
form {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }
form>button{
    margin-top: 15px;
}
</style>
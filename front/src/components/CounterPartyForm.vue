<template>
    <div>
        <h3>Добавление контрагента</h3>
        <form @submit.prevent>
            <InputUI
              v-model.trim="counterparty.cp_name"
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
    props:{
        id:{
            type: Number,
            required: true,
        }
    },
    data(){
        return{
            counterparty: {
                cp_name:"",
                cost:"Отсутствует",
            }
        };
    },
    methods:{
        createCounterParty(){ 
            this.counterparty.id=this.id+1;
            this.$emit("create", this.counterparty);
            this.postCounterParty();
            this.counterparty = {         
                cp_name:'',
            };
        },
        async postCounterParty(){
            const requestOptions = {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ cp_name: this.counterparty.cp_name })
            };
            console.log(this.counterparty.cp_name);
            const response = await fetch("http://127.0.0.1:8000/api/counterparty/", requestOptions);
            const data = await response.json();
            console.log(data);
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
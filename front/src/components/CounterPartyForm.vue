<template>
    <div>
        <h3>Добавление контрагента</h3>
        <form @submit.prevent>
            <div v-show="haveErrors&&this.errors.name!=null" class="">{{this.errors.name}}</div>
            <InputUI
              v-model.trim="counterparty.name"
              type="text"
              required
              placeholder="Имя контрагента"/>
              <div v-show="haveErrors&&this.errors.score!=null" class="">{{this.errors.score}}</div>
              <InputUI
              v-model.trim="counterparty.score"
              type="text"
              required
              placeholder="Цена закрытия"/>
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
                name:"",
                score:"",
            },
            haveErrors:false,
            errors:{},
        };
    },
    methods:{
        createCounterParty(){ 
            this.postCounterParty();
            this.haveErrors = true
        },
        async postCounterParty(){
            const requestOptions = {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ name: this.counterparty.name,
                                        score: this.counterparty.score })
            };
            const response = await fetch("http://127.0.0.1:8000/api/counterparty/", requestOptions);
            const data = await response.json();
            this.errors = data
            if (response.status==201){
                this.$emit("create", this.counterparty);
                this.counterparty = {         
                    name:'',
                    score:''
                };
            }
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
    background-color: #0079C2;
    color: white !important;
}
form>div{
    margin-bottom: 10px;
    color:red
}
h3{margin-bottom: 15px;}
</style>
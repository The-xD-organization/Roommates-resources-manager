<template>
    <div>
        <b-spinner
            v-if="$store.state.getTaskStatus == 0"
            variant="info"
            label="Spinning"
        >
        </b-spinner>
        <p v-if="$store.state.getTaskStatus == -1">Błąd ładowania</p>
        <div v-else>
            <h5>Wyświetlaj:</h5>
            <label class="container">Niezrobione
                <input type="checkbox" id="notDone" value="true" v-model="notDone">
                <span class="checkmark"></span>
            </label>
            <label class="container">Zrobione
                <input type="checkbox" id="done" value="true" v-model="done">
                <span class="checkmark"></span>
            </label>
            <div
                v-for="task in $store.state.tasksList" :key = task.id
            >
                <ShowTask
                    v-bind:task="task"
                    v-if="(done == task.is_done || notDone == !task.is_done)
                        && !(notDone == false && done == false)"
                />
            </div>
        </div>
    </div>
</template>

<script>
import ShowTask from '@/components/tasks/ShowTask.vue';

export default {
    name: 'TasksList',
    components: {
        ShowTask,
    },
    data() {
        return {
            notDone: true,
            done: false,
        };
    },
    mounted() {
        this.$store.dispatch('getTasks');
    },
};

</script>

<style scoped>
.container {
  display: block;
  position: relative;
  padding-left: 35px;
  margin-bottom: 12px;
  cursor: pointer;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}
/*ukrycie domyślnego checkmarka*/
.container input {
  position: absolute;
  opacity: 0;
  cursor: pointer;
  height: 0;
  width: 0;
}

.checkmark {
  position: absolute;
  top: 0;
  left: 0;
  height: 25px;
  width: 25px;
  background-color: #eee;
}

.container:hover input ~ .checkmark {
  background-color: #ccc;
}

.container input:checked ~ .checkmark {
  background-color: #17a2b8;
}

.checkmark:after {
  content: "";
  position: absolute;
  display: none;
}

.container input:checked ~ .checkmark:after {
  display: block;
}

.container .checkmark:after {
  left: 10px;
  top: 6px;
  width: 5px;
  height: 10px;
  border: solid white;
  border-width: 0 3px 3px 0;
  -webkit-transform: rotate(45deg);
  -ms-transform: rotate(45deg);
  transform: rotate(45deg);
}
</style>

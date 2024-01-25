<template>
    <div class="login">
        <el-card class="box_card">
            <div slot='header' class='clearfix'>
                <span>系统</span>
            </div>
            <el-form :model="form" ref="form" label-width="80px" class="demo-ruleForm">
                <el-form-item label="用户名" prop="username" :rules="[
                    { required: true, message: '请输入用户名' },
                    {
                        min: 4,
                        max: 10,
                        message: '长度在4-10位之间'
                    }
                ]">
                    <el-input type="text" v-model="form.username"></el-input>
                </el-form-item>
                <el-form-item label="密码" prop="password" :rules="[
                    { required: true, message: '请输入密码' },
                    {
                        min: 6,
                        max: 12,
                        message: '长度在6-12位之间'
                    }
                ]">
                    <el-input type="password" v-model="form.password"></el-input>
                </el-form-item>
                <el-form-item>
                    <el-button type="primary" @click="login('form')">登录</el-button>
                </el-form-item>
            </el-form>
        </el-card>

    </div>
</template>

<script>
export default {
    name: 'Login',
    data() {
        return {
            form: {
                username: '',
                password: ''
            }
        }
    },
    methods: {
        login(form) {
            this.$refs[form].validate((valid) => {
                if (valid) {
                    this.$router.push('/home')
                } else {
                    console.error(this.form)
                }
            })
        }
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.login {
    width: 100%;
    height: 100%;
    position: absolute;
    background: #40d9ff;
}

.login .box_card {
    width: 450px;
    margin: 200px auto;
}

.login .box_card .el-card__header {
    font-size: 34px;
}

.login .box_card .el-button {
    width: 100%;
}
</style>

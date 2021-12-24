<script>

export default {
  props: {
    deviceId: {
      type: String,
      required: true
    },
    deviceUrl: {
      type: String,
      required: true
    }
  }
}
</script>

<template>
<div class="col-12 col-md-6 d-flex align-items-stretch">
    <div class="card col-12">
      <div class="card-header">
        <h2 class="header-title">
          <a class="badge badge-light" href="" target="_blank">
            <i class="mdi mdi-printer-3d"></i> {{device.hostname}} - {{ device.updated_dt | naturaltime }}</a>

          </a>
        </h2>
      </div>
        <div class="card-body">
            <div class="col-6 offset-3 mt-2">
            <img src="/static/images/sleep.svg" style="opacity: 30%" class="d-none d-md-block img-fluid"/>
            </div>
            <a href="#" target="_blank">
                <button class="btn btn-light btn-sm mr-2 ml-2">
                <i class="mdi mdi-camera"></i> Start Monitoring
                </button>
            </a>
        </div>
        <div class="card-footer d-flex justify-content-center">
            <a href="">
                <button class="btn btn-primary btn-sm mr-2 ml-2" id="start-monitoring">
                <i class="mdi mdi-camera"></i> Add New Camera
                </button>
            </a>
            <a href="" target="_blank">
                <button class="btn btn-light btn-sm mr-2 ml-2">
                    <i class="mdi mdi-printer-3d"></i> Manage Pi
                </button>
            </a>
        </div>
    </div>
</div>
</template>

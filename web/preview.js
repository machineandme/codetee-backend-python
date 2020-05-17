var firstRun = true
var s = location.pathname.split("/")
s = s.pop() || s.pop()


let wap = new Vue({
  el: "#app",
  data: {
    buy: false,
    thx: false,
    title: "Teeeee with code!",
    text: s.split("_")[0],
    color: s.split("_")[1],
    ig: "",
    email: "",
    phone: "",
  },
  methods: {
    submit: function() {
        this.buy = false
        this.thx = true
        let response = fetch('/checkout', {
          method: 'POST',
          body: JSON.stringify({
            which: s,
            ig: this.ig,
            email: this.emil,
            phone: this.phone
          })
        })
    },
    teeShot: function() {
        var imgData = renderer.domElement.toDataURL()
        var linkDown = document.createElement("a")
        linkDown.download = s + ".png"
        linkDown.href = imgData
        document.body.appendChild(linkDown)
        linkDown.click()
        document.body.removeChild(linkDown)
    }
  }
})

// /*


import * as THREE from '/such_static/three/build/three.module.js'

import { DDSLoader } from '/such_static/three/examples/jsm/loaders/DDSLoader.js'
import { MTLLoader } from '/such_static/three/examples/jsm/loaders/MTLLoader.js'
import { OBJLoader } from '/such_static/three/examples/jsm/loaders/OBJLoader.js'


let container

let camera, scene, renderer

let mouseX = 0, mouseY = 0
let rh = new Date().getTime()
let sized

if (window.innerWidth < window.innerHeight) {
  sized = window.innerWidth
} else {
  sized = window.innerHeight
}

let windowHalfX = sized / 2
let windowHalfY = sized / 2


init()
animate()


function init() {

  container = document.getElementById('tee-view-3d')
  // document.body.appendChild(container)

  camera = new THREE.PerspectiveCamera(45, sized / sized, 1, 2000)
  camera.position.z = 250

  // scene

  scene = new THREE.Scene()

  let ambientLight = new THREE.AmbientLight(0xcccccc, 0.8)
  scene.add(ambientLight)

  let pointLight = new THREE.PointLight(0xffffff, 0.5)
  camera.add(pointLight)
  scene.add(camera)

  // model

  let onProgress = function (xhr) {

    if (xhr.lengthComputable) {

      // let percentComplete = xhr.loaded / xhr.total * 100
      // console.log(Math.round(percentComplete, 2) + '% downloaded')

    }

  }

  let onError = function () { }

  let manager = new THREE.LoadingManager()
  manager.addHandler(/\.dds$/i, new DDSLoader())

  // comment in the following line and import TGALoader if your asset uses TGA textures
  // manager.addHandler( /\.tga$/i, new TGALoader() )

  const base_mtl = '/shirt/' + s + '/'
  const mtl_file = '6_OBJ_T-shirts.mtl'
  const obj_file = '6_OBJ_T-shirts.obj'
  new MTLLoader(manager)
    .setPath(base_mtl)
    .load(mtl_file, function (materials) {

      materials.preload()
      for (const material in materials["materials"]) {
        materials["materials"][material].side = THREE.DoubleSide
      }

      new OBJLoader(manager)
        .setMaterials(materials)
        .setPath(base_mtl)
        .load(obj_file, function (object) {

          // object.position.x = 60
          // object.position.y = -170
          // object.scale.x = .2
          // object.scale.y = .2
          // object.scale.z = .2
          let mod = 1
          object.position.x = 60 * mod
          object.position.y = -170 * mod
          object.scale.x = .2 * mod
          object.scale.y = .2 * mod
          object.scale.z = .2 * mod
          scene.add(object)

        }, onProgress, onError)

    })

  //

  renderer = new THREE.WebGLRenderer({ alpha: true, preserveDrawingBuffer: true  })
  // renderer.setClearColor(0x000011, 0.1)
  renderer.setClearColor(0x000000, 0)
  renderer.setPixelRatio(window.devicePixelRatio)
  renderer.setSize(sized, sized)
  container.appendChild(renderer.domElement)

  document.addEventListener('mousemove', onDocumentMouseMove, false)

  //

  window.addEventListener('resize', onWindowResize, false)

}

function onWindowResize() {

  if (window.innerWidth < window.innerHeight) {
    sized = window.innerWidth
  } else {
    sized = window.innerHeight
  }

  windowHalfX = sized / 2
  windowHalfY = sized / 2

  camera.aspect = sized / sized
  camera.updateProjectionMatrix()

  renderer.setSize(sized, sized)

}

function onDocumentMouseMove(event) {

  mouseX = (event.clientX - windowHalfX) / 2
  mouseY = (event.clientY - windowHalfY) / 2

}

//

function animate() {

  requestAnimationFrame(animate)
  render()

}


function render() {
  // let de = renderer.domElement
  if (firstRun || renderer.domElement.matches(':hover')) {
    if (!firstRun) {
    camera.position.x = renderer.domElement.offsetLeft - mouseX
    camera.position.z = 200 + renderer.domElement.offsetTop - mouseY
    }
    let centa = new THREE.Vector3(scene.position.x, scene.position.y, scene.position.z)
    camera.lookAt(centa)

    renderer.render(scene, camera)
    setTimeout(()=>{
        firstRun = false
    }, 5000)
  }
}

// */
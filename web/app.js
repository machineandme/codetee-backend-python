const EXTS = [".ada", ".b", ".b", ".c", ".c++", ".cc", ".cmake", ".cmd", ".cs", ".css", ".cxx", ".d", ".dart", ".diff", ".dmesg", ".docker", ".ex", ".g", ".go", ".gradle", ".groovy", ".hh", ".html", ".inf", ".jade", ".java", ".js", ".json", ".less", ".lisp", ".lua", ".m", ".php", ".phtml", ".rb", ".scala", ".scss", ".sql", ".swift", ".tf", ".toml", ".ts", ".twig", ".v", ".vala", ".vb", ".vim", ".xml", ".yaml", ".zsh"]
const FNFIR = ["abominable", "absolute", "absurd", "acceptable", "accurate", "actual", "adult", "advanced", "advantageous", "aged", "agitated", "ancient", "appalled", "approximate", "aromatic", "arrogant", "artificial", "astonished", "average", "awed", "bad", "baked", "basic", "bitter", "blunt", "boastful", "boring", "brave", "brief", "bright", "broad", "busy", "calculating", "calm", "can", "capable", "careless", "certain", "cheap", "cheerful", "clean", "cold", "competitive", "complete", "complex", "concave", "conditional", "confident", "conic", "considerate", "constant", "contented", "continuous", "convex", "cooked", "cool", "cooperative", "correct", "crazy", "creative", "cubic", "cunning", "curious", "damaged", "dangerous", "deaf", "decent", "deep", "defective", "dejected", "delightful", "depressed", "desirable", "difficult", "diligent", "disadvantageous", "distressed", "divorced", "doubtful", "dreamy", "dry", "early", "easy", "efficient", "emaciated", "emotional", "engaged", "enterprising", "equal", "erudite", "essential", "even", "exact", "excellent", "excessive", "excited", "exhausted", "expensive", "experienced", "faithful", "false", "fantastic", "far", "fat", "fearful", "final", "fine", "fragrant", "free", "frequent", "fresh", "fried", "friendly", "frightened", "full", "fuming", "future", "gifted", "glad", "good", "great", "greedy", "grown", "guilty", "haggard", "handsome", "happy", "hard", "harmful", "harmless", "healthy", "honest", "horizontal", "horrified", "hospitable", "hot", "huge", "humid", "hungry", "hurt", "hysterical", "ignorant", "illegal", "illogical", "imaginary", "important", "impudent", "inclined", "incomplete", "incorruptible", "industrious", "inexperienced", "inferior", "infrequent", "infuriated", "initial", "insignificant", "insufficient", "intact", "interesting", "invalid", "irritable", "late", "lazy", "lean", "little", "logical", "lonely", "long", "loud", "lovey", "low", "lucky", "mad", "married", "mature", "maximum", "mediocre", "minimum", "modest", "moved", "muffled", "naive", "narrow", "natural", "near", "necessary", "negative", "negligent", "nervous", "nice", "noisy", "normal", "numerous", "observant", "obsolete", "obstinate", "occasional", "occupied", "old", "optimistic", "optimum", "outgoing", "oval", "particular", "past", "peevish", "perfect", "periodical", "persistent", "pessimistic", "pleasant", "positive", "practical", "preceding", "precise", "pregnant", "preliminary", "present", "pretty", "previous", "profitable", "pungent", "purposeful", "quick", "quiet", "ragged", "rapid", "rare", "raw", "ready", "real", "recent", "rectangular", "redundant", "regular", "rejected", "relative", "reliable", "repulsive", "reserved", "respectful", "responsible", "rich", "robust", "rough", "round", "sad", "salty", "sarcastic", "satisfactory", "satisfied", "secondary", "self", "selfish", "separate", "serious", "shallow", "sharp", "shocked", "shocking", "short", "shy", "significant", "similar", "simultaneous", "single", "slim", "slow", "sly", "smelly", "smooth", "sociable", "soft", "sophisticated", "sorrowful", "sorry", "sour", "special", "specific", "spherical", "spoiled", "spoilt", "square", "stable", "standard", "startled", "stinking", "straight", "strange", "strong", "stuffed", "stunned", "sudden", "sufficient", "superfluous", "superior", "surprised", "sweet", "talented", "talkative", "tall", "tasteless", "terrified", "theoretical", "thick", "thin", "thirsty", "thorough", "tired", "tiresome", "tolerant", "touching", "tough", "traditional", "triangular", "true", "trusting", "typical", "ugly", "unattractive", "uneven", "unhappy", "uninterrupted", "unpleasant", "unprofitable", "upset", "urgent", "useful", "useless", "usual", "vacant", "valid", "vertical", "vigorous", "warm", "weak", "well", "wet", "wise", "wonderful", "woozy", "worried", "wrong", "young"]
const FNSEC = ["app", "module", "script", "example", "index", "style", "test", "view"]

function choose(choices) {
  let index = Math.floor(Math.random() * choices.length)
  return choices[index]
}

function makeFileTypes() {
  let result = []
  for (let i = 0; i < 1; i++) {
    let mr = Math.random()
    if (mr < .1) {
      let s = choose(FNSEC)
      s = s.charAt(0).toUpperCase() + s.slice(1)
      result.push(choose(FNFIR) + s + choose(EXTS))
    } else if (mr < .2) {
      result.push((choose(FNFIR) + "_" + choose(FNSEC) + choose(EXTS)).toUpperCase())
    } else {
      result.push(choose(FNFIR) + "_" + choose(FNSEC) + choose(EXTS))
    }
  }
  return result.join(", ")
}

let wap = new Vue({
  el: "#app",
  data: {
    fileType: makeFileTypes()
  }
})

setInterval(() => {
  wap.fileType = makeFileTypes()
}, 2000)

// /*


import * as THREE from './three/build/three.module.js'

import { DDSLoader } from './three/examples/jsm/loaders/DDSLoader.js'
import { MTLLoader } from './three/examples/jsm/loaders/MTLLoader.js'
import { OBJLoader } from './three/examples/jsm/loaders/OBJLoader.js'


let container

let camera, scene, renderer

let mouseX = 0, mouseY = 0
let rh = new Date().getTime()
let sized

if (window.innerWidth < window.innerHeight) {
  sized = window.innerWidth / 2
} else {
  sized = window.innerHeight / 2
}

let windowHalfX = sized / 2
let windowHalfY = sized / 2


init()
animate()


function init() {

  container = document.getElementById('tee-view-3d')
  document.body.appendChild(container)

  camera = new THREE.PerspectiveCamera(45, sized / sized, 1, 2000)
  camera.position.z = 250

  // scene

  scene = new THREE.Scene()

  let ambientLight = new THREE.AmbientLight(0xcccccc, 0.4)
  scene.add(ambientLight)

  let pointLight = new THREE.PointLight(0xffffff, 0.8)
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

  const base_mtl = '/shirt/'
  const mtl_file = '6_OBJ_T-shirts.mtl?' + rh
  const obj_file = '6_OBJ_T-shirts.obj?' + rh
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

          object.position.x = 60
          object.position.y = -170
          object.scale.x = .2
          object.scale.y = .2
          object.scale.z = .2
          scene.add(object)

        }, onProgress, onError)

    })

  //

  renderer = new THREE.WebGLRenderer({ alpha: true })
  renderer.setClearColor(0x000011, 0.1)
  // renderer.setClearColor(0x000000, 0)
  renderer.setPixelRatio(window.devicePixelRatio)
  renderer.setSize(sized, sized)
  container.appendChild(renderer.domElement)

  document.addEventListener('mousemove', onDocumentMouseMove, false)

  //

  window.addEventListener('resize', onWindowResize, false)

}

function onWindowResize() {

  if (window.innerWidth < window.innerHeight) {
    sized = window.innerWidth / 2
  } else {
    sized = window.innerHeight / 2
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
  if (renderer.domElement.matches(':hover')) {
    camera.position.x = renderer.domElement.offsetLeft - mouseX
    let centa = new THREE.Vector3(scene.position.x, scene.position.y, scene.position.z)
    camera.lookAt(centa)

    renderer.render(scene, camera)
  }
}

// */
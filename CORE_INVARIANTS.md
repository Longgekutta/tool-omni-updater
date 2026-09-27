# 核心使命不变量 (CORE_INVARIANTS.md)

> **版本**：1.0.0-PROD  
> **生效范围**：`tool-omni-updater` 仓库全域  
> **主权属性**：本文件为项目根目录**刚性只读契约**，任何 AI 集群节点或人类开发者在扩展本工程时必须 100% 遵守以下核心不变量。

---

## 🏛️ 不变量一：唯一本体定位与领域防腐 (Domain Purity & Anti-Bleed)
1. **专精单一职责**：全域开源软件资产自治、逆向嗅探与无感升级中枢；
2. **手绝不伸过界**：严禁侵入操作系统官方包管理器（Apt/Pacman/Winget 官方商店源）已成熟管辖的领地，专精于“直接源自 GitHub/GitLab Releases 的独立、便携与绿色资产”；
3. **极速启动与纯净依赖**：核心嗅探与调度算法 100% 优先采用原生轻量标准库，冷启动时延严格控制在亚 50ms。

---

## ⚡ 不变量二：物理验真不变量 (Proof-of-Truth Invariant)
1. 任何平台的更新替换逻辑（Windows 文件锁绕过、Linux 赋权、Android 安装通道、macOS 磁盘挂载）必须在沙箱或真实环境中伴随确定性自动化回归测试用例；
2. 无法自动化物理验真的平台逻辑等同于不可用代码。

---

## 🛡️ 不变量三：凭证与安全隔离不变量 (Secret & Security Isolation)
1. 任何 GitHub Token、私有 Gist 凭证严禁硬编码提交；
2. 下载的二进制文件在执行覆盖前，必须进行哈希校验（SHA256）与安全沙箱隔离核验，杜绝中间人劫持与投毒风险。

---

## ⚙️ 不变量四：平台解耦微逻辑不变量 (Platform Specialization Invariant)
1. 核心业务（API 解析、SemVer 对比、定时调度、AI 提纯）必须维持 100% 跨平台统一；
2. 平台专属执行端（Windows / Linux / Android / macOS）必须保持物理解耦，严禁跨平台脏逻辑互相渗漏。

---

## 🧭 不变量五：三位一体正交协同 (Trinity Orthogonal Synergy)
1. 脱离全家桶可独立自洽运行；
2. 对外输出强类型标准化数据契约（`.provenance.json`、`manifest.json`），充当下游开发者工作流的确定性底座。

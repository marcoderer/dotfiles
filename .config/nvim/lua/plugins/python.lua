return {
  {
    "williamboman/mason.nvim",
    opts = function(_, opts)
      table.insert(opts.ensure_installed, "black")
    end,
  },
  {
    "stevearc/conform.nvim",
    optional = true,
    opts = {
      formatters_by_ft = {
        ["python"] = { "black" },
      },
    },
  },
  {
    "fisadev/vim-isort",
    ft = "python",
    config = function()
      -- disable default keybinding
      vim.g.vim_isort_map = ""
      -- automatically format file buffer on save
      vim.api.nvim_create_autocmd({ "BufWritePre" }, {
        pattern = "*.py",
        callback = function()
          vim.cmd("Isort")
        end,
      })
    end,
  },
  {
    "psf/black",
    config = function()
      vim.api.nvim_create_autocmd({ "BufWritePre" }, {
        pattern = "*.py",
        callback = function()
          vim.cmd("Black")
        end,
      })
    end,
  },
}
